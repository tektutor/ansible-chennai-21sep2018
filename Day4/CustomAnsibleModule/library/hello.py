from ansible.module_utils.basic import AnsibleModule

class Hello:
   def sayHello(self, msg):
       return msg

def main():
 
    module = AnsibleModule(
		argument_spec=dict(
			message = dict(type='str', required=True)
	        )
             )

    msg = module.params['message']

    objHello = Hello()
    greeting_msg = objHello.sayHello( msg )

    module.exit_json ( meta=greeting_msg, changed=True, rc=0 )

main()
