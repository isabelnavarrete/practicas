import logging

from app import db, app

if __name__ == '__main__':
	logging.info('>>>>>>>>>> INIT CREATE ALL DB <<<<<<<<<<')
	app.app_context().push()
	db.create_all()
	logging.info('>>>>>>>>>> FINISH CREATE ALL DB <<<<<<<<<<')