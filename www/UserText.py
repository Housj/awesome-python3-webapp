# -*- coding: utf-8 -*-

import orm
import asyncio
import sys
from Model import User,Blog,Comment

@asyncio.coroutine
def test(loop):
	yield from orm.create_pool(loop=loop,user='root',password='jlcroot',db='awesome')
	u = User(name='sergei',email='18211016323@163.com',passwd='111111',image='about:blank')
	yield from u.save()
	#users = yield from User.findAll()
	#print(users)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([test(loop)]))
	loop.close()
	if loop.is_closed():
	    sys.exit(0)
