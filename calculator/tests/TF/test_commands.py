from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch, MagicMock, call
from calculator.management.commands.freelance_calculate import Command
from calculator.config import Messages


class TestFreelanceCalculateCommand(TestCase):
    @patch("calculator.management.commands.freelance_calculate.Command.get_input")
    @patch("calculator.management.commands.freelance_calculate.Command.write_output")
    def test_no_style_argument(self, mock_write_output, mock_get_input):
        mock_get_input.side_effect = [
            "500",
            "5",
            "non",
        ]
        call_command("freelance_calculate", no_style=True)

    @patch("calculator.management.commands.freelance_calculate.Command.get_input")
    @patch("calculator.management.commands.freelance_calculate.Command.write_output")
    def test_default_style_behavior(self, mock_write_output, mock_get_input):
        mock_get_input.side_effect = [
            "500",
            "5",
            "oui",
            "4",
        ]
        call_command("freelance_calculate")

    @patch(
        "calculator.management.commands.freelance_calculate.Command.get_input",
        side_effect=["500", "5", "oui", "4"],
    )
    def test_main_yes_option(self, mock_input):
        command = Command()
        command.stdout = MagicMock()
        command.handle(no_style=True)

        expected_calls = [
            call(Messages.REM_TITLE),
            call(Messages.MONTHLY_INCOME.format("10000.0")),
            call(Messages.NEW_DAR.format(4, "625.0")),
        ]

        command.stdout.write.assert_has_calls(expected_calls, any_order=False)

    @patch(
        "calculator.management.commands.freelance_calculate.Command.get_input",
        side_effect=["500", "5", "non"],
    )
    def test_main_no_option(self, mock_input):
        command = Command()
        command.stdout = MagicMock()
        command.handle(no_style=True)

        expected_calls = [
            call(Messages.REM_TITLE),
            call(Messages.MONTHLY_INCOME.format("10000.0")),
            call(Messages.NO_MODIFICATION),
        ]

        command.stdout.write.assert_has_calls(expected_calls, any_order=False)
