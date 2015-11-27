from fabric.api import run, local, env #setting  ImportError: cannot import name setting

def host_type():
    run('uname -s')

def hello():
	print("Hell world")


def chaos():
	local('date')

def deploy(m='fixed problem'):
	'''
	deploy:m="COMMIT LOG" \t(defalut as "fixed problem") 
	'''
	_git(m)

def _touch(m='fixed problem'):
	local('pwd'
			'&& touch git.log'
			'&& echo "{msg}" >> git.log'.format(msg=m)
			)


def _git(m='Fix problem'):
	'''
	git:m="COMMIT LOG" \t(defalut as "fixed problem") 
	'''
	local('pwd'
			'&& touch git.log'
			'&& echo "{msg}" >> git.log'
			'&& git add ..'
			'&& git commit -am "{msg} @Cen"'
			'&& git push'
			'&& date'.format(msg=m)
			)

