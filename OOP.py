class Primary:
    def pri(self):
        print("Hey dear")


class Secondary(Primary):
    _num = 10
    def sec(self, x):
        self.num = x
        return x


s = Secondary()
s.pri()
print(s._num)
print(s.sec(20))
