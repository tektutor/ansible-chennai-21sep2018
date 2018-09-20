from ansible.module_utils.basic import AnsibleModule

def add(val1, val2):
    return val1 + val2

def main():
    module = AnsibleModule(
		argument_spec=dict(
			firstValue = dict(type='float', required=True),
			secondValue = dict(type='float', required=True)
	        )
             )

    value1 = module.params['firstValue']
    value2 = module.params['secondValue']

    result = add( value1, value2 )

    #The line below reports a success with the result
    module.exit_json ( meta=result, changed=False, rc=0 )

    #The line below reports a failure with a message
    #module.fail_json ( '***Critial error happend***' )

main()
