'''
I have imported unittest library. There are 7 test cases defined here that help us understand.
'''


import unittest

def getData(data, keys):
    if len(keys) == 0 or keys[0] == "/":
        raise KeyError("Null or invalid key passed")

    keyArray = keys.split("/")
    currObj = data

    for key in keyArray:
        if key not in currObj:
            raise KeyError("Key not found. Key is:", key)

        currObj = currObj[key]

    return currObj

data = {
    "a": {
        "b": {
            "c": "a_b_c",
            "d": "a_b_d",
            "e": "a_b_e"
            },
        "c": {
            "d": "a_c_d"
            }
        }
    }

class Tests(unittest.TestCase):
    def test_nullKey(self):
        with self.assertRaises(KeyError, msg='Null or invalid key passed'):
            getData(data, "")

    def test_forwardSlashKey(self):
        with self.assertRaises(KeyError, msg='Null or invalid key passed'):
            getData(data, "/")

    def test_invalidKey(self):
        with self.assertRaises(KeyError, msg='Null or invalid key passed'):
            getData(data, "/a/b")

    def test_invalidKey2(self):
        with self.assertRaises(KeyError, msg='Key not found. Key is: d'):
            getData(data, "/a/b/c/d/e")

    def test_success1(self):
        self.assertEqual(getData(data, "a/b/c"), 'a_b_c')

    def test_success2(self):
        self.assertEqual(getData(data, "a/c/d"), 'a_c_d')

    def test_success3(self):
        self.assertEqual(getData(data, "a/b"), {
            "c": "a_b_c",
            "d": "a_b_d",
            "e": "a_b_e"
            })

if __name__ == '__main__':
    unittest.main()
