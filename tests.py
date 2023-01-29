import json
import unittest
import requests


class WorkOrderResolverTestCase(unittest.TestCase):
    def setUp(self):
        self.endpoint_url = 'http://127.0.0.1:5000/graphql'
        self.headers = {'content-type': 'application/json'}

    def test_create_customer(self):
        query = """
            mutation newCustomer {
                createCustomer(
                    first_name: "Mike"
                    last_name: "Doyle"
                    address: "First Street"
                    email: "mike@doyle.com"
                    phone_number: "111"
                ) {
                id
                first_name
                last_name
                address
                email
                phone_number
                }
            }
        """

        response = requests.post(
            self.endpoint_url,
            json={'query': query},
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.text)
        self.assertEqual(json_response['data']['createCustomer']['address'], 'First Street')
        self.assertEqual(json_response['data']['createCustomer']['email'], 'mike@doyle.com')
        self.assertEqual(json_response['data']['createCustomer']['first_name'], 'Mike')
        self.assertEqual(json_response['data']['createCustomer']['last_name'], 'Doyle')
        self.assertEqual(json_response['data']['createCustomer']['phone_number'], '111')

    def test_create_work_order(self):
        query = """
            mutation {
                createWorkOrder(type: Service, schedule: "tomorrow", customerId: 1) {
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

        response = requests.post(
            self.endpoint_url,
            json={'query': query},
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.text)
        self.assertEqual(json_response['data']['createWorkOrder']['customer']['first_name'], 'Mike')
        self.assertEqual(json_response['data']['createWorkOrder']['schedule'], 'tomorrow')

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

        response = requests.get(
            self.endpoint_url,
            json={'query': query},
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
