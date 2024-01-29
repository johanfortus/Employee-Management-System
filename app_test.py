from app import app, db, Data
from flask import url_for
from unittest import TestCase

class EmployeeManagementSystemTestCase(TestCase):
    
    def test_employee_management_system_status(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)

     # Set up a test client and test database 
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

     # Tear down the test database and client 
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Create test employee
    def test_update_employee(self):
        test_employee = Data(name='Test User', email='test@test.com', phone='1234567890')
        db.session.add(test_employee)
        db.session.commit()

        # Update test employee
        with app.test_client() as client:
            res = client.post('/update', data={
                'id': test_employee.id,
                'name': 'Updated Name',
                'email': 'updated@test.com',
                'phone': '0987654321'
            }, follow_redirects=True)
            self.assertIn('Employee Updated Successfully', res.get_data(as_text=True))

    # Create and delete test employee
    def test_delete_employee(self):

        # Create a test employee
        test_employee = Data(name='Test User', email='test@test.com', phone='1234567890')
        db.session.add(test_employee)
        db.session.commit()

        # Delete the test employee
        with app.test_client() as client:
            res = client.get(f'/delete/{test_employee.id}', follow_redirects=True)
            self.assertIn('Employee Deleted Successfully', res.get_data(as_text=True))

    # Test Data model
    def test_data_model(self):
        new_employee = Data(name='Test Employee', email='test@example.com', phone='1234567890')
        self.assertEqual(new_employee.name, 'Test Employee')
        self.assertEqual(new_employee.email, 'test@example.com')
        self.assertEqual(new_employee.phone, '1234567890')

    def test_home_page_elements(self):
        with app.test_client() as client:
            res = client.get('/')
            data = res.get_data(as_text=True)
            self.assertIn('<h1 class="modal-title fs-5" id="ModalLabel">Add Employee</h1>', data)
            self.assertIn('<input type="text" class="form-control" id="inputName"', data)
            self.assertIn('<input type="text" class="form-control" id="inputEmail"', data)
            self.assertIn('<input type="text" class="form-control" id="inputPhone"', data)
            self.assertIn('<button type="submit" class="btn btn-primary">Add Employee</button>', data)

    def test_update_modal_elements(self):
        with app.test_client() as client:
            res = client.get('/')
            data = res.get_data(as_text=True)
            self.assertIn('<h1 class="modal-title fs-5" id="ModalLabel">Update Employee</h1>', data)
            self.assertIn('<button type="submit" class="btn btn-primary">Update</button>', data)

    def test_employee_table_structure(self):
        with app.test_client() as client:
            res = client.get('/')
            data = res.get_data(as_text=True)
            self.assertIn('<th scope="col">ID</th>', data)
            self.assertIn('<th scope="col">Name</th>', data)
            self.assertIn('<th scope="col">Email</th>', data)
            self.assertIn('<th scope="col">Phone</th>', data)
            self.assertIn('<th scope="col">Action</th>', data)
    
    # Check for delete buttons (assuming there is an employee in the database)
    def test_delete_buttons(self):
        with app.test_client() as client:
            res = client.get('/')
            data = res.get_data(as_text=True)
            self.assertIn('btn btn-danger', data)
            self.assertIn('onclick="return confirm(\'Are you sure you want to delete?\')"', data)

    # Post a new employee to generate a flash message
    def test_flash_messages_after_insert(self):
        with app.test_client() as client:
            client.post('/insert', data={
                'name': 'Test Employee',
                'email': 'test@test.com',
                'phone': '1234567890'
            }, follow_redirects=True)

            res = client.get('/')
            data = res.get_data(as_text=True)

            # Check for flash message
            self.assertIn('Employee Inserted Successfully', data)

if __name__ == '__main__':
    unittest.main()