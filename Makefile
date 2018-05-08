BUILD_NUMBER ?= 0

dev:
	yarn install
	grunt
rpm:
	rpmbuild -bb globalnoc-table-panel.spec --define "_sourcedir ${PWD}" --define="_buildno ${BUILD_NUMBER}"
