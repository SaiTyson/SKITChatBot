"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial avatarions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.config.base import BaseContainerConfigurationData

class KikConfiguration(BaseContainerConfigurationData):

    def __init__(self):
        BaseContainerConfigurationData.__init__(self, "kik")
        self._bot_name = "program-y"
        self._webhook = "https://localhost:5000"
        self._host = "0.0.0.0"
        self._port = 5000
        self._debug = False
        self._workers = 4
        self._ssl_cert_file = None
        self._ssl_key_file = None

    @property
    def bot_name(self):
        return self._bot_name

    @property
    def webhook(self):
        return self._webhook

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def debug(self):
        return self._debug

    @property
    def workers(self):
        return self._workers

    @property
    def ssl_cert_file(self):
        return self._ssl_cert_file

    @property
    def ssl_key_file(self):
        return self._ssl_key_file

    def load_configuration(self, configuration_file, bot_root):
        kik = configuration_file.get_section(self.section_name)
        if kik is not None:
            self._bot_name = configuration_file.get_option(kik, "bot_name", missing_value="program-y")
            self._webhook = configuration_file.get_option(kik, "webhook", missing_value="https://localhost:5000")
            self._host = configuration_file.get_option(kik, "host", missing_value="0.0.0.0")
            self._port = configuration_file.get_option(kik, "port", missing_value=5000)
            self._debug = configuration_file.get_bool_option(kik, "debug", missing_value=False)
            self._workers = configuration_file.get_option(kik, "workers", missing_value=4)
            self._ssl_cert_file = configuration_file.get_option(kik, "ssl_cert_file")
            if self._ssl_cert_file is not None:
                self._ssl_cert_file = self.sub_bot_root(self._ssl_cert_file, bot_root)
            self._ssl_key_file = configuration_file.get_option(kik, "ssl_key_file")
            if self._ssl_key_file is not None:
                self._ssl_key_file = self.sub_bot_root(self._ssl_key_file, bot_root)
