ABS_DIR = $(shell pwd)


PROJECT_NAME    = UnclePy
2d_SRCDIR       = two_d
3d_SRCDIR       = three_d
DOCDIR          = docs


SPHINX_SOURCEDIR  = $(DOCDIR)
SPHINX_BUILDDIR   = $(DOCDIR)/build
SPHINX_RSTDIR     = $(DOCDIR)/rst
SPHINX_OPTS       =


.PHONY: run2d
run2d:
	@python -m $(2d_SRCDIR).run

.PHONY: test2d
test2d:
	@python -m unittest $(2d_SRCDIR).tests -v


.PHONY: run3d
run3d:
	@cd $(3d_SRCDIR)/build && cmake .. && make && ./unclepy

#.PHONY: test3d
#test3d: testgrid testsnake
#	@python -m unittest $(SRCDIR).tests -v


.PHONY: doc
doc:
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/exceptions $(SRCDIR)/exceptions
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/grid $(SRCDIR)/grid
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/tests $(SRCDIR)/tests
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR) $(SRCDIR)
	@make sphinx c=html
	@google-chrome $(ABS_DIR)/$(SPHINX_BUILDDIR)/html/index.html

# make sphinx c=help
.PHONY: sphinx
sphinx:
	@python -msphinx -M $(c) "$(SPHINX_SOURCEDIR)" "$(SPHINX_BUILDDIR)" $(SPHINX_OPTS)
