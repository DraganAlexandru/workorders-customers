import json
import unittest
import requests


class WorkOrderResolverTestCase(unittest.TestCase):
    def setUp(self):
        self.endpoint_url = 'http://127.0.0.1:5000/graphql'

    def test_create_work_order(self):
        query = """
            mutation {
                createWorkOrder(type: Service, schedule: "tomorrow", customerId: 2) {
                    id
                    schedule
                    customer {
                        id
                        first_name
                        last_name
                        email
                        phone_number
                        address
                    }
                }
            }
        """

        headers = {'content-type': 'application/json'}
        response = requests.post(
            self.endpoint_url,
            json={'query': query},
            headers=headers
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.text)
        data = json_response["data"]
        print(data)
        # self.assertEqual(json_response['data']['createWorkOrder']['workOrder']['type'], 'Service')
        # self.assertEqual(json_response['data']['createWorkOrder']['workOrder']['schedule'], 'tomorrow')

    def test_retrieve_all_work_orders(self):
        query = """
            query fetchAllWorkOrders {
                workOrders {
                    id
                    schedule
                    customer {
                        first_name
                        last_name
                        address
                        email
                        phone_number
                    }
                }
            }
        """

        headers = {'content-type': 'application/json'}
        response = requests.get(
            self.endpoint_url,
            json={'query': query},
            headers=headers
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
