#!/usr/bin/env python3
"""Lab 2.3: Skills System - Starter Template

Complete the TODOs to implement the lab requirements.
"""

from signalwire_agents import AgentBase


class SkillsAgent(AgentBase):
    def __init__(self):
        super().__init__(name="skills-agent", route="/agent")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant with access to various skills. "
            "Use your skills to help users with time and math calculations."
        )

        self.add_language("English", "en-US", "rime.spore")

        # TODO: Add built-in skills using self.add_skill()
        # Available skills include:
        # - "datetime" - provides get_current_time and get_current_date
        # - "math" - provides calculate function
        #
        # Example:
        # self.add_skill("datetime", {"timezone": "America/New_York"})
        # self.add_skill("math")


agent = SkillsAgent()

if __name__ == "__main__":
    agent.run()
