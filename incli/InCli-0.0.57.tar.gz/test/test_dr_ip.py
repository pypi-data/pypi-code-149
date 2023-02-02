import unittest,simplejson
from InCli import InCli
from InCli.SFAPI import file,DR_IP,restClient,query,utils

class Test_DR_IP(unittest.TestCase):
    options = {
        "isDebug": True,
        "chainable": True,
        "resetCache": False,
        "ignoreCache": True,
        "queueableChainable": False,
        "useQueueableApexRemoting": False
    }     
    def test_IP(self):
        restClient.init('DTI')
        
        call = DR_IP.ip("custom_GetTrialPromos",input={},options=self.options)

        print()

    def test_IP_test(self):
        restClient.init('DTI')

        input = {
            "cartId": "8010Q0000035ec1QAA"
        }
        
        call = DR_IP.ip("unai_chainableIpsTest",input=input,options=self.options)

        print()

    key ='206b7636-e00b-d789-ce3f-f5f751c7479a'
    def test_attachment(self):
        restClient.init('DTI')

        q = f"select fields(all) from vlocity_cmt__DRBulkData__c where vlocity_cmt__GlobalKey__c = '{self.key}' limit 20"
        call0 = query.query(q)
        print(call0)
        
        q2 = f"select fields(all) from Attachment where ParentId ='{call0['records'][0]['Id']}' limit 10"
        call2 = query.query(q2)
        print(call2['records'][0]['Id'])
        attachmentId = call2['records'][0]['Id']
     #   attachmentId = '00P0Q00000JWEzGUAX'
        action = f"/services/data/v55.0/sobjects/Attachment/{attachmentId}/Body"
        call = restClient.requestWithConnection(action=action)

        print()

    def test_finish_call(self):
        restClient.init('DTI')
        input = "{}"

        options1 = self.options.copy()
        options1['vlcIPData'] = self.key

        call = DR_IP.ip("custom_GetTrialPromos",input=input,options=options1)

        print()

    def test_dr_bundle(self):
        restClient.init('DTI')

        q = "SELECT Name, Id, LastModifiedDate, LastModifiedBy.Name, CreatedDate, CreatedBy.Name, vlocity_cmt__Type__c, vlocity_cmt__InputType__c, vlocity_cmt__OutputType__c, vlocity_cmt__Description__c, LastModifiedById FROM vlocity_cmt__DRBundle__c USING SCOPE Everything WHERE vlocity_cmt__Type__c != 'Migration' AND  vlocity_cmt__Type__c != 'Export (Component)' ORDER BY Name"

        q = "SELECT Name, Id, LastModifiedDate, LastModifiedBy.Name, CreatedDate, CreatedBy.Name, vlocity_cmt__Type__c, vlocity_cmt__InputType__c, vlocity_cmt__OutputType__c, vlocity_cmt__Description__c, LastModifiedById FROM vlocity_cmt__DRBundle__c ORDER BY Name"


        res = query.query(q)
        
        out = []
        for record in res['records']:
            o = {
                "Name":record['Name'],
                "type":record['vlocity_cmt__Type__c']

            }
            out.append(o)
        utils.printFormated(out)
        print()