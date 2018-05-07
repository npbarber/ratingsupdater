NOSETESTS ?= $(shell sh -c 'which nosetests 2>/dev/null || echo nosetests')

test:
	$(NOSETESTS) --with-doctest tests $(test_flags)
