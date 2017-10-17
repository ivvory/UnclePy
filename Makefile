ABS_DIR = $(shell pwd)


PROJECT_NAME = UnclePy
SRCDIR       = src
DOCDIR       = docs


SPHINX_SOURCEDIR  = $(DOCDIR)
SPHINX_BUILDDIR   = $(DOCDIR)/build
SPHINX_RSTDIR     = $(DOCDIR)/rst
SPHINX_OPTS       =


.PHONY: run
run:
	@python -m src.main


.PHONY: doc
doc:
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/exceptions $(SRCDIR)/exceptions
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/grid $(SRCDIR)/grid
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/tests $(SRCDIR)/tests
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR) $(SRCDIR)
	@make sphinx c=html
	@google-chrome $(ABS_DIR)/$(SPHINX_BUILDDIR)/html/index.html


.PHONY: test
test: testgrid testsnake
	@python -m unittest src.tests -v

.PHONY: testgrid
testgrid:
	@python -m unittest src.tests.test_grid -v

.PHONY: testsnake
testsnake:
	@python -m unittest src.tests.test_snake -v

.PHONY: testfood
testfood:
	@python -m unittest src.tests.test_food -v


# make sphinx c=help
.PHONY: sphinx
sphinx:
	@python -msphinx -M $(c) "$(SPHINX_SOURCEDIR)" "$(SPHINX_BUILDDIR)" $(SPHINX_OPTS)
