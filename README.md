# Work Orders Customers GraphQL Flask

## **Implemented the functionality of**
- create new work orders
- retrieve a work order by ID
- retrieve all work orders

## **Installation**
Clone the repo

`git clone`

Navigata to the root

`cd workorders_customers`

Create a virtualenv

`python3 -m venv workorders_env`

Install required packages

`pip3 install -r requirements.txt`

## **Running the app**

`export export FLASK_APP=main`

Start the server

`flask run`

Open the GraphQL PlayGround by visiting http://127.0.0.1:5000/graphql

Query to retrieve all the available work orders:

```buildoutcfg
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
```

Query to retrieve a work order based on ID

```buildoutcfg
query fetchWorkOrder {
  workOrder(workOrderId: "1") {
    id 
    schedule
    customer {
      first_name
      last_name
      email
      address
      phone_number
    } 
  }
}
```

Mutation to create a new work order

```buildoutcfg
mutation newWorkOrder {
  createWorkOrder(type: Service, schedule: "tomorrow", customerId: "3") {
    id
    schedule
    customer {
      first_name
      last_name
      email
      phone_number
      address
    }
  }
}

```

Mutation to create a new customer

```buildoutcfg
mutation newCustomer{
  createCustomer(first_name: "Mike", last_name: "Doyle", address: "Second Street", email: "mike@doyle.com", phone_number: "777") {
    id
    first_name
    last_name
    address
    email
    phone_number
}
```