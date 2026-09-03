"""
Prompt Registry - Manage and retrieve prompts
"""

import logging
from typing import Dict, Optional
from .system_prompts import SYSTEM_PROMPTS, TASK_PROMPTS

logger = logging.getLogger(__name__)


class PromptRegistry:
    """
    Registry for managing system and task prompts
    """

    def __init__(self):
        self.system_prompts: Dict[str, str] = SYSTEM_PROMPTS.copy()
        self.task_prompts: Dict[str, str] = TASK_PROMPTS.copy()
        self.custom_prompts: Dict[str, str] = {}

    def get_system_prompt(self, prompt_type: str = "base") -> str:
        """Get system prompt by type"""
        prompt = self.system_prompts.get(prompt_type)
        if not prompt:
            logger.warning(f"System prompt '{prompt_type}' not found, using base")
            return self.system_prompts.get("base", "")
        return prompt

    def get_task_prompt(self, task_type: str, **kwargs) -> Optional[str]:
        """Get task prompt with variable substitution"""
        template = self.task_prompts.get(task_type)
        if not template:
            logger.warning(f"Task prompt '{task_type}' not found")
            return None

        try:
            return template.format(**kwargs)
        except KeyError as e:
            logger.error(f"Missing variable in task prompt: {e}")
            return None

    def register_custom_prompt(self, name: str, prompt: str) -> bool:
        """Register custom system prompt"""
        if name in self.system_prompts or name in self.task_prompts:
            logger.warning(f"Cannot override built-in prompt '{name}'")
            return False

        self.custom_prompts[name] = prompt
        logger.info(f"Registered custom prompt: {name}")
        return True

    def get_custom_prompt(self, name: str) -> Optional[str]:
        """Get custom prompt"""
        return self.custom_prompts.get(name)

    def list_system_prompts(self) -> list:
        """List available system prompt types"""
        return list(self.system_prompts.keys())

    def list_task_prompts(self) -> list:
        """List available task prompt types"""
        return list(self.task_prompts.keys())

    def list_custom_prompts(self) -> list:
        """List custom prompts"""
        return list(self.custom_prompts.keys())


class PromptBuilder:
    """
    Builder for constructing complete prompts
    Combines system prompt, context, and instructions
    """

    def __init__(self, registry: PromptRegistry):
        self.registry = registry

    def build_prompt(
        self,
        system_type: str = "base",
        user_level: Optional[str] = None,
        context: Optional[Dict] = None,
        task: Optional[str] = None,
        task_params: Optional[Dict] = None,
    ) -> str:
        """Build complete prompt with context"""
        parts = []

        # 1. System prompt
        system_prompt = self.registry.get_system_prompt(system_type)
        parts.append(system_prompt)

        # 2. User level adaptation
        if user_level:
            level_guidance = self._get_level_guidance(user_level)
            if level_guidance:
                parts.append(f"\nUser Level: {user_level.upper()}")
                parts.append(level_guidance)

        # 3. Context
        if context:
            context_str = self._build_context_str(context)
            if context_str:
                parts.append(f"\nContext:\n{context_str}")

        # 4. Task-specific instructions
        if task:
            task_prompt = self.registry.get_task_prompt(task, **(task_params or {}))
            if task_prompt:
                parts.append(f"\nTask Instructions:\n{task_prompt}")

        return "\n".join(parts)

    def _get_level_guidance(self, user_level: str) -> Optional[str]:
        """Get guidance for user level"""
        guidance = {
            "beginner": "Explain concepts simply. Use analogies and examples. Assume no prior knowledge.",
            "intermediate": "Provide technical details. Explain the 'why' behind recommendations.",
            "professional": "Focus on efficiency, edge cases, and advanced configurations.",
        }
        return guidance.get(user_level.lower())

    def _build_context_str(self, context: Dict) -> str:
        """Build context string from dictionary"""
        lines = []
        if "project" in context:
            lines.append(f"Project: {context['project'].get('name', 'Unknown')}")
        if "objective" in context:
            lines.append(f"Objective: {context['objective']}")
        if "constraints" in context:
            lines.append(f"Constraints: {', '.join(context['constraints'])}")
        return "\n".join(lines) if lines else ""


# Global registry instance
prompt_registry = PromptRegistry()
prompt_builder = PromptBuilder(prompt_registry)
