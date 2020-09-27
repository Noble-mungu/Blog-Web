from flask_script import Manager,Server
from app.models import User
from app import create_app

app = create_app()
manager.add_command(Server())

@manager.shell
def make_shell_context():
	return dict(app = app,User = User)

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)


if __name__ == '__main__':
    manager.run()