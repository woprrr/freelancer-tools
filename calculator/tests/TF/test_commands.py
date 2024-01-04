from django.test import TestCase
from unittest.mock import patch, MagicMock, call
from calculator.management.commands.freelance_calculate import Command
from calculator.config import Messages


class TestFreelanceCalculateCommand(TestCase):
    ANSI_SUCCESS_PREFIX = "\x1b[32;1m"
    ANSI_RESET_SUFFIX = "\x1b[0m"

    @patch("builtins.input", side_effect=["500", "5", "oui", "4"])
    def test_main_yes_option(self, mock_input):
        command = Command()
        command.stdout = MagicMock()
        command.handle()

        expected_calls = [
            call(Messages.REM_TITLE),
            call(
                self.ANSI_SUCCESS_PREFIX
                + Messages.MONTHLY_INCOME.format("10000.0")
                + self.ANSI_RESET_SUFFIX
            ),
            call(
                self.ANSI_SUCCESS_PREFIX
                + Messages.NEW_DAR.format(4, "625.0")
                + self.ANSI_RESET_SUFFIX
            ),
        ]

        command.stdout.write.assert_has_calls(expected_calls, any_order=False)

    @patch("builtins.input", side_effect=["500", "5", "non"])
    def test_main_no_option(self, mock_input):
        command = Command()
        command.stdout = MagicMock()
        command.handle()

        expected_calls = [
            call(Messages.REM_TITLE),
            call(
                self.ANSI_SUCCESS_PREFIX
                + Messages.MONTHLY_INCOME.format("10000.0")
                + self.ANSI_RESET_SUFFIX
            ),
            call(Messages.NO_MODIFICATION),
        ]

        command.stdout.write.assert_has_calls(expected_calls, any_order=False)
