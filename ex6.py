#-*- coding:utf-8 -*-
x="There are %d types of people."%10
binary='binary'
do_not="don't"
y="Those who know %s and thoes who %s"%(binary,do_not)
print x
print y

print "I said:%r"%x
print "I said:%s"%y

hilarious=False
joke_ecaluation="Isn't that joke of funny? %r"
#内嵌了%r

print joke_ecaluation %hilarious

w="This is the left side of..."
e="a strint with a right side."

print w+e

