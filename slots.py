from rasa.core.slots import Slot


class ViewSlot(Slot):

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value == "shipped order":
                r[0] = 1.0
            elif self.value == "style number":
                r[1] = 1.0
            else:
                r[2] = 1.0
        return r


class AddDeleteSlot(Slot):

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value == "size" or self.value == "color" or self.value == "country":
                r[0] = 1.0
            elif self.value == "style":
                r[1] = 1.0
            else:
                r[2] = 1.0
        return r