PYTHON=py -3.7

exec_targets=\
	checker.exe \
	dist_standalone.exe \
	patcher.exe  \
	run_wizard.exe \
	run_wizard_gui.exe 

mod_release_targets=\
	hiveswap \
	openbound \
	pq_betas \
	pq_trolls \
	intro \
	sandbox \
	sbb \
	variants

all: doc exe mods

lite.zip: lite/*
	-rm -v lite.zip
	pushd lite; zip ../lite.zip -8 -r *.* */; popd

clean:
	$(RM) -r __pycache__
	$(RM) -r build/
	$(RM) -r dist/
	$(RM) -r lite/
	$(RM) -r ../litedist/

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

mods: $(addsuffix .zip,$(addprefix ../release/,${mod_release_targets}))

../release/%.zip: ../custom_volumes_other/%
	${PYTHON} package_rpa.py $(notdir $<)
	mkdir -vp ../release
	zip $@ -8 -r ../custom_volumes/$(notdir $<)_min/

../release/%.zip: ../custom_volumes/%
	mkdir -vp ../release
	zip $@ -8 -r ../custom_volumes/$(notdir $<)/

.PHONY: all clean exe doc mods