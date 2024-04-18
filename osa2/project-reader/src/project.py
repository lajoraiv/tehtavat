class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        output ="\n"
        for i in range(len(dependencies)):
            output = output + "- " + dependencies[i] + "\n"
        return output if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name.capitalize()}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            "\n"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
