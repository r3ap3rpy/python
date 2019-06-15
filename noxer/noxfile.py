import nox

@nox.session(name = "test_sample.py")
def tests(session):
    session.run("pytest", external = True)

@nox.session(name = "another")
@nox.parametrize(
            'requests',
            [
                nox.param('2.21.0', id = 'latest'),
                nox.param('2.20.0', id = 'previous'),
                ]
        )
def tests(session, requests):
    session.install(f"requests=={requests}")
    session.run("pytest")

@nox.session(name='more')
@nox.parametrize('additional',['request','bs4'])
@nox.parametrize(
            'requests',
            [
                nox.param('2.21.0', id = 'latest'),
                nox.param('2.20.0', id = 'previous'),
                ]
        )
def tests(session, additional, requests):
    session.install(f"requests=={requests}")
    session.install(f"{additional}")
    session.run('pytest')
