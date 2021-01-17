# This File reads an XMI model and provides a M2M transformation to
# generate to for a RosBridge model. Actually implements the 
# GeneROS - RosBridge integration wihin an MDE transformation, from 
# model to model.
#
# Written in 16/1/2021
# Written by Rafael Brouzos
#
# The generated RosBridge model from the GeneROS model can be found in
# the "generos/models" path
#
# Therefore, you can use it in RosBridge as described in the tool's
# official documentation

from pyecoregen.ecore import EcoreGenerator 
from weasyprint import HTML
import subprocess
import sys
import networkx as nx
import matplotlib.pyplot as plt 

import os
from pyecore.resources import ResourceSet, URI, global_registry
from pyecore.resources.json import JsonResource
from pyecore.ecore import EClass, EAttribute
import pyecore.ecore as Ecore
import pyecore.behavior as behavior
from pyecore.utils import DynamicEPackage
from jinja2 import Environment, FileSystemLoader
sys.path.append(os.path.join(os.path.dirname(__file__),'metamodelLib'))

# ~ import metamodel
# ~ import metageneros

# Obtain App Install directory
install_dir = str(os.path.dirname(__file__))

# Obtain arguments
generos_dir = os.path.relpath(sys.argv[1], install_dir)
# ~ destination = os.path.relpath(sys.argv[2], install_dir)
# ~ broker_info = os.path.relpath(sys.argv[3], install_dir)
metamodel_filename = os.path.join(sys.argv[1], 'metamodelLib/metageneros.ecore')
print(metamodel_filename)
model_filename = os.path.join(sys.argv[1], 'models/generos.xmi')

# Go to working directory
if install_dir != '':
	os.chdir(install_dir)
	
# Create rset and load Metamodel
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
# If you work with python package metamodel uncomment following line
# ~ rset.metamodel_registry[metamodel.nsURI] = metamodel
# if you with .ecore file metamodel uncomment following 3 lines
resource = rset.get_resource(URI(metamodel_filename))
root = resource.contents[0]
rset.metamodel_registry[root.nsURI] = root

# We obtain the model from an XMI
model_root = rset.get_resource(URI(model_filename)).contents[0]


# Load the templates
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader,trim_blocks=True, lstrip_blocks=True)


# ROS2 system (ROSConnection)
ros2_connections = []
ros2_connection = {}
ros2_connection['name'] = 'LocalROSConn'




# Initialize
topic_bridges = []
service_bridges = []

# Iterate in the packages
for package in model_root.hasSoftware.hasPackages:
	if package.name == "interfaces" or package.name.startswith('launch') or package.builtin == True:
		continue
	# Iterate in Nodes
	for node in package.hasNodes:
		# Iterate in Publishers
		for p in node.hasPublishers:
			topic_bridge = {}
			# Add TopicBridge (R2B)
			if p.pmsg.__class__.__name__ == "CustomMessage":
				topic_bridge['msgType'] = 'interfaces/'+p.pmsg.name
			else:
				topic_bridge['msgType'] = '/'+p.pmsg.package+'/'+p.pmsg.name
			topic_bridge['name'] = p.name+'_bridge'
			topic_bridge['rosConn'] = 'LocalROSConn'
			topic_bridge['rosURI'] = p.topicPath
			topic_bridge['brokerConn'] = 'TODO'
			topic_bridge['brokerURI'] = 'TODO'
			topic_bridge['direction'] = 'R2B'
			# Append it to the rest
			topic_bridges.append(topic_bridge)
			
		# Iterate in Subscribers
		for s in node.hasSubscribers:
			topic_bridge = {}
			# Add TopicBridge (B2R)
			if s.smsg.__class__.__name__ == "CustomMessage":
				topic_bridge['msgType'] = 'interfaces/'+s.smsg.name
			else:
				topic_bridge['msgType'] = '/'+s.smsg.package+'/'+s.smsg.name
			topic_bridge['name'] = s.name+'_bridge'
			topic_bridge['rosConn'] = 'LocalROSConn'
			topic_bridge['rosURI'] = s.topicPath
			topic_bridge['brokerConn'] = 'TODO'
			topic_bridge['brokerURI'] = 'TODO'
			topic_bridge['direction'] = 'B2R'
			# Append it to the rest
			topic_bridges.append(topic_bridge)
			
		# Iterate in Clients
		for c in node.hasClients:
			service_bridge = {}
			# Add ServiceBridge (R2B)
			if c.servicemessage.__class__.__name__ == "CustomService":
				service_bridge['msgType'] = '/interfaces/'+c.servicemessage.name
			else:
				service_bridge['msgType'] = '/'+c.servicemessage.package+'/'+c.servicemessage.name
			service_bridge['name'] = c.name+'_bridge'
			service_bridge['rosConn'] = 'LocalROSConn'
			service_bridge['rosURI'] = c.serviceName
			service_bridge['brokerConn'] = 'TODO'
			service_bridge['brokerURI'] = 'TODO'
			service_bridge['direction'] = 'R2B'
			# Append it to the rest
			service_bridges.append(service_bridge)
			
		# Iterate in Servers
		for s in node.hasServers:
			service_bridge = {}
			# Add ServiceBridge (B2R)
			if s.servicemessage.__class__.__name__ == "CustomService":
				service_bridge['msgType'] = '/interfaces/'+s.servicemessage.name
			else:
				service_bridge['msgType'] = '/'+s.servicemessage.package+'/'+s.servicemessage.name
			service_bridge['name'] = s.name+'_bridge'
			service_bridge['rosConn'] = 'LocalROSConn'
			service_bridge['rosURI'] = s.serviceName
			service_bridge['brokerConn'] = 'TODO'
			service_bridge['brokerURI'] = 'TODO'
			service_bridge['direction'] = 'B2R'
			# Append it to the rest
			service_bridges.append(service_bridge)

# Generate model.rbr
# ___________________________________________
# Load the Template of the model.rbr 
template = env.get_template('temp_rosbridge.rbr')
# Fire up the rendering proccess
output = template.render(ros2_connections=ros2_connections, topic_bridges=topic_bridges, service_bridges=service_bridges)
	
# Write the generated file
dest='models/model.rbr'
with open(dest, 'w') as f:
	f.write(output)

# Give execution permissions to the generated python file
os.chmod(dest, 509)




