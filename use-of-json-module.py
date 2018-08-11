#uses of json module
import json

params = {
    'parameters':[
        {
            'ob_job_id': 'test'
        }
    ]
}

print "params: ",params

print "json dump param: ",json.dumps(params)


print "job_Id: {}".format(params['parameters'][0]['ob_job_id'])
