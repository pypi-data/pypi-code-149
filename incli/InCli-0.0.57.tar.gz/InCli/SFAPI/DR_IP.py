from . import restClient,utils
import simplejson
#------------------------------------------------------------------------------------------------------------------------------------------------
def dr(bundleName,inputData):
   """
   - bundleName: Name of the Data Raptor Bundle
   - inputData: input Data to the DR
   """
   action = f'/services/apexrest/{restClient.getNamespace()}/v2/DataRaptor'

   data = {
       "bundleName" : bundleName, 
       "objectList": inputData
   }
   call = restClient.callAPI(action, method="post", data=data)
   return call
#------------------------------------------------------------------------------------------------------------------------------------------------
def ipResponse(name,input,options=None,field=None):
   """
   Calls the IP and returns the response object
   - name: type_subtype
   - input: input data json.
   - options: the options json. 
   - field: if specified will return the value of the 'field' in response.  
   """
   res = ip(name,input,options)
   IPResult = res['IPResult']
   if 'response' in IPResult:
      IPResult = IPResult['response']

   if field != None and field in IPResult:
      return IPResult[field]
   return IPResult
#------------------------------------------------------------------------------------------------------------------------------------------------
def ip(name,input,options=None):
   """
   Calls the IP 
   - name: type_subtype
   - input: input data json.
   - options: the options json. 
   """
   action = f'/services/apexrest/vlocity_cmt/v1/GenericInvoke/vlocity_cmt.IntegrationProcedureService/{name}'
   data = {
      "sMethodName":name,
      "sClassName":"vlocity_cmt.IntegrationProcedureService",
      }

   if type(input) is dict:
      input = simplejson.dumps(input)

   data['input'] = input
   if options == None:
      options = "{}"
   else:
      if type(options) is dict:
         options = simplejson.dumps(options)      
   data['options'] =  options


   call = restClient.callAPI(action=action,data=data,method='post')
   utils.printJSON(call)
   #print(call)
   return call
#------------------------------------------------------------------------------------------------------------------------------------------------
def ip_response(call,field=None):
   IPResult = call['IPResult']
   if 'response' in IPResult:
      IPResult = IPResult['response']

   if field != None and field in IPResult:
      return IPResult[field]
   return IPResult
#------------------------------------------------------------------------------------------------------------------------------------------------
def call_chainable_ip(name,input,options=None):
   action = f'/services/apexrest/callipasynch/v1/{name}'
   action = f'/services/apexrest/callip/v1/{name}'
   action = f'/services/apexrest/callip/v2/{name}'
   action = f'/services/apexrest/callip/v3/{name}'

   data = {
      "sMethodName":name,
      "sClassName":"vlocity_cmt.IntegrationProcedureService",
      }

   data['input'] = input
   if options == None:
      options = {}
   data['options'] =  options


   call = restClient.callAPI(action=action,data=data,method='post')
   return call
#------------------------------------------------------------------------------------------------------------------------------------------------
def remoteClass(className,method,input,options=None):
   """
   Calls a remote APEX class inside Salesforce 
   - className: the callable APEX class name
   - method: the method to invoke.
   - input: the options json. 
   - options: the options json 
   """
   action = f'/services/apexrest/vlocity_cmt/v1/GenericInvoke/{className}/{method}'

   if type(input) is dict:
      input = simplejson.dumps(input)

   if options == None:
      options = {
         "postTransformBundle":"",
         "preTransformBundle":"",
         "useQueueableApexRemoting":False,
         "ignoreCache":False,
         "vlcClass":"B2BCmexAppHandler",
         "useContinuation":False
         }         
      
   data = {
      "sMethodName":method,
      "sClassName":className,
      "input":input,
      "options":simplejson.dumps(options)
      }

   call = restClient.callAPI(action=action,data=data,method='post')
   return call