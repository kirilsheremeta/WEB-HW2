from prettytable import PrettyTable


class PrettyView:
    def create_table(self, data):
        raise NotImplementedError

    def create_row(self, data):
        raise NotImplementedError


class AddressBookView(PrettyView):
    def create_table(self, data):
        result = PrettyTable()
        result.field_names = ["Name", "Birthday", "Email", "Address", "Phone"]
        for i in data:
            result.add_row(i)
        return result

    def create_row(self, data):
        result = PrettyTable()
        result.field_names = ["Name", "Birthday", "Email", "Address", "Phone"]
        result.add_row(data)
        return result


class NoteBookView(PrettyView):
    def create_table(self, data):
        result = PrettyTable()
        result.field_names = ["Index", "Tags", "Note"]
        for i in data:
            result.add_row(i)
        return result

    def create_row(self, data):
        result = PrettyTable()
        result.field_names = ["Index", "Tags", "Note"]
        result.add_row(data)
        return result


class SortDirectoryView(PrettyView):
    def create_row(self, data):
        result = PrettyTable()
        result.field_names = ["Known_extensions", "Unknown_extensions"]
        result.add_row(data)
        return result

    def create_table(self, data):
        pass
