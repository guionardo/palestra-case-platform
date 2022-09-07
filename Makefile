build_uml:
	@echo "Building UML"
	@./run-plantuml.sh -tsvg /work/palestra/docs/*.puml -o /work/palestra/images
	@echo "Done"

build: build_uml
	cd palestra; npm run build; npm run build_pack