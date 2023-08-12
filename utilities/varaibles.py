import json
import os

class Variables:
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file = os.path.join(root_dir, "config/config.json")

    with open(config_file,'r') as f:
        conf = json.load(f)
        
    smtp_host = conf['smtp_host']
    smtp_port = conf['smtp_port']
    email_sender = conf['email_username']
    email_sender_password = conf['email_password']
    email_receivers = conf['email_receivers']
    
    def __getitem__(self,key):
        """Get Value from key"""
        return self.conf[key]
    
try:
    var = Variables()
    
except Exception as e:
    raise e

