def get_recovery_protocol(stress_level):
    """Deterministic logic gate for burnout intervention."""
    
    if stress_level > 7:
        return {
            "tier": "LEVEL 3: HARD RESET",
            "tone": "Your hardware is redlining. If you don't pick a rest day, your body will pick it for you.",
            "actions": [
                "Activate 'Emergency Sick Day' (No Slack/Email).",
                "Full digital detox for 12 hours.",
                "Execute 9-hour sleep cycle immediately."
            ]
        }
    elif 4 <= stress_level <= 7:
        return {
            "tier": "LEVEL 2: PERFORMANCE MAINTENANCE",
            "tone": "You're at high RPM. We need to trim the scope to prevent a crash.",
            "actions": [
                "Delete 2 non-essential tasks from today's list.",
                "Implement 50/10 Pomodoro (no exceptions).",
                "Move one meeting to 'Asynchronous' (Email/Loom)."
            ]
        }
    else:
        return {
            "tier": "LEVEL 1: OPTIMIZED STEADY-STATE",
            "tone": "Systems nominal. Let's keep this pace sustainable.",
            "actions": [
                "Standard hydration check.",
                "Logout at exactly 5:00 PM.",
                "Log one 'Small Win' to cement progress."
            ]
        }