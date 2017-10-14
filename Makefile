ABS_DIR = $(shell pwd)


PROJECT_NAME = UnclePy
SRCDIR       = src
DOCDIR       = docs


SPHINX_SOURCEDIR  = $(DOCDIR)/source
SPHINX_BUILDDIR   = $(DOCDIR)/_build
SPHINX_RSTDIR     = $(SPHINX_SOURCEDIR)/rst
SPHINX_OPTS       =


.PHONY: run
run:
	@python -m src.main


.PHONY: doc
doc:
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/exceptions $(SRCDIR)/exceptions
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR)/tests $(SRCDIR)/tests
	@sphinx-apidoc -f -o $(SPHINX_RSTDIR) $(SRCDIR)
	@make sphinx c=html
	@google-chrome $(ABS_DIR)/$(SPHINX_BUILDDIR)/html/index.html


# make sphinx c=help
.PHONY: sphinx
sphinx:
	@python -msphinx -M $(c) "$(SPHINX_SOURCEDIR)" "$(SPHINX_BUILDDIR)" $(SPHINX_OPTS)


#https://developer.ridgerun.com/wiki/index.php/How_to_generate_sphinx_documentation_for_python_code_running_in_an_embedded_system#Generating_.rst_files