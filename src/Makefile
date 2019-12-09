PYTHON=py -3.7

exec_targets=\
	checker.exe \
	dist_standalone.exe \
	package.exe  \
	patcher.exe  \
	pesterlog_to_rpy.exe \
	run_wizard.exe \
	run_wizard_gui.exe 

all: doc exe

clean:
	$(RM) -r __pycache__
	$(RM) -r build
	$(RM) -r dist/
	$(RM) -r litedist/

exe: $(addprefix bin/,${exec_targets})

bin/%.exe: ../src/%.py
	${PYTHON} -m PyInstaller \
		--onefile \
		--console \
		--distpath ../bin \
		--workpath build \
		--specpath build \
		--name $(notdir $@) \
		$<

doc:
	cd ../doc && ./make.sh

.PHONY: all clean exe doc