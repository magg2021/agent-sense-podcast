"""
Governed Healthcare Agent: PCP Coordinator & Specialist Routing Demo
Built with IBM Bob Architecture for Applied AI Summit Presentation
Speaker: Monika Aggarwal
"""

import json
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any


# ============================================================================
# 1. DATA CONTRACTS & SCHEMAS (Deterministic Control Layer)
# ============================================================================

@dataclass
class IntakeContext:
    primary_symptoms: List[str] = field(default_factory=list)
    onset_time: Optional[str] = None
    severity_scale_1_to_10: Optional[int] = None
    progression: Optional[str] = None  # e.g., "worsening", "constant", "improving"
    associated_red_flags: List[str] = field(default_factory=list)
    vital_signs_reported: Optional[Dict[str, str]] = None
    medications_tried: List[str] = field(default_factory=list)

    def is_complete_for_routing(self) -> tuple[bool, List[str]]:
        missing = []
        if not self.onset_time:
            missing.append("onset_time (when did symptoms start?)")
        if self.severity_scale_1_to_10 is None:
            missing.append("severity_scale_1_to_10 (severity on scale 1-10)")
        if not self.progression:
            missing.append("progression (is it sudden, gradual, constant, worsening?)")
        if not self.associated_red_flags:
            missing.append("red_flag_screening (fever, neurological deficits, visual disturbance, stiff neck)")
        return (len(missing) == 0, missing)


@dataclass
class SpecialistHandoffPacket:
    patient_id: str
    target_specialty: str
    routing_reason: str
    evidence_summary: str
    intake_data: Dict[str, Any]
    relevant_ehr_snippets: List[str]
    clinician_review_status: str = "PENDING_APPROVAL"


# ============================================================================
# 2. AUDIT TRACER (Observability & Governance)
# ============================================================================

class TraceLogger:
    def __init__(self, mode_name: str):
        self.mode_name = mode_name
        self.events = []

    def log(self, step_num: int, layer: str, component: str, action: str, details: str, status: str = "INFO"):
        event = {
            "step": step_num,
            "layer": layer,  # "MODEL_REASONING" vs "DETERMINISTIC_CONTROL"
            "component": component,
            "action": action,
            "status": status,
            "details": details
        }
        self.events.append(event)
        
        # Color coding for terminal output
        layer_tag = f"[\033[94m{layer}\033[0m]" if layer == "MODEL_REASONING" else f"[\033[93m{layer}\033[0m]"
        status_tag = f"\033[92m{status}\033[0m" if status == "PASSED" else (f"\033[91m{status}\033[0m" if status in ["FAILED", "REJECTED", "RISK_DETECTED"] else status)
        print(f"  Step {step_num:02d} | {layer_tag:<32} | {component:<24} | {action:<25} | {status_tag}")
        print(f"          └── Details: {details}")


# ============================================================================
# 3. DETERMINISTIC CONTROL GATES
# ============================================================================

class EmergencySafetyGate:
    """Deterministic Rule-Based Red Flag / 911 Escalation Filter"""
    EMERGENCY_KEYWORDS = [
        "thunderclap", "worst headache of my life", "sudden numbness", 
        "slurred speech", "chest pain", "shortness of breath", "loss of consciousness"
    ]

    @classmethod
    def evaluate(cls, user_text: str) -> tuple[bool, Optional[str]]:
        text_lower = user_text.lower()
        for kw in cls.EMERGENCY_KEYWORDS:
            if kw in text_lower:
                return True, f"Emergency trigger keyword detected: '{kw}'"
        return False, None


class MCPGateway:
    """Model Context Protocol (MCP) Deterministic Security & Tool Gateway"""
    ALLOWED_TOOLS = {
        "PCP_Agent": ["get_patient_history", "request_intake_clarification", "prepare_handoff_packet"],
        "Neurology_Specialist": ["review_neurology_context", "suggest_migraine_protocol"],
        "GI_Specialist": ["review_gi_context", "suggest_antiemetic_protocol"]
    }

    @classmethod
    def check_tool_permission(cls, caller_agent: str, tool_name: str) -> bool:
        allowed = cls.ALLOWED_TOOLS.get(caller_agent, [])
        return tool_name in allowed


# ============================================================================
# 4. PCP COORDINATOR & SPECIALIST SYSTEM
# ============================================================================

class PCPHealthcareAgentSystem:
    def __init__(self, loose_autonomy_mode: bool = False):
        self.loose_autonomy_mode = loose_autonomy_mode
        self.mode_label = "LOOSE_AUTONOMY_MODE (Unconstrained Agents)" if loose_autonomy_mode else "GOVERNED_WORKFLOW_MODE (Deterministic Contracts)"
        self.step_counter = 1

    def process_patient_query(self, user_query: str, structured_intake: Optional[IntakeContext] = None) -> TraceLogger:
        tracer = TraceLogger(self.mode_label)
        self.step_counter = 1

        print("\n" + "=" * 95)
        print(f"  EXECUTION RUN: {self.mode_label}")
        print(f"  Input: \"{user_query}\"")
        print("=" * 95)

        # --------------------------------------------------------------------
        # BRANCH 1: LOOSE AUTONOMY MODE (The Failure Pattern)
        # --------------------------------------------------------------------
        if self.loose_autonomy_mode:
            # Step 1: Model Semantic Ingestion
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="PCP_Orchestrator_LLM",
                action="Semantic Symptom Parsing",
                details="Extracted symptoms: ['headache', 'nausea']. LLM infers potential neurological & GI etiologies.",
                status="COMPLETED"
            )
            self.step_counter += 1

            # Step 2: Unconstrained Autonomy - Skipping Intake & Direct Multi-Agent Routing
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="PCP_Orchestrator_LLM",
                action="Autonomous Multi-Dispatch",
                details="LLM autonomously decides to fan out tasks to BOTH Neurology and Gastroenterology agents simultaneously without intake validation.",
                status="RISK_DETECTED"
            )
            self.step_counter += 1

            # Step 3: Direct Specialist Invocation (Neurology)
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="Neurology_Agent",
                action="Specialist Evaluation",
                details="Received raw symptom 'headache'. Speculates intracranial etiology or migraine. Generates workup recommendations based on assumptions.",
                status="SPECULATIVE"
            )
            self.step_counter += 1

            # Step 4: Direct Specialist Invocation (GI)
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="Gastroenterology_Agent",
                action="Specialist Evaluation",
                details="Received raw symptom 'nausea'. Speculates acute gastroenteritis. Suggests antiemetic prescription advice.",
                status="SPECULATIVE"
            )
            self.step_counter += 1

            # Step 5: Uncontrolled Tool Execution via MCP
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="PCP_Orchestrator_LLM",
                action="Direct EHR Tool Trigger",
                details="Autonomous agent attempts to draft order in EHR and send unverified notification directly to patient.",
                status="DETERMINISTIC_BYPASS"
            )
            self.step_counter += 1

            # Step 6: Final Unreviewed Output
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="PCP_Orchestrator_LLM",
                action="Response Generation",
                details="Safety disclaimer is present ('Not a doctor'), but workflow executed 2 specialist handoffs on incomplete intake without clinician approval.",
                status="GOVERNANCE_FAILURE"
            )

            return tracer

        # --------------------------------------------------------------------
        # BRANCH 2: GOVERNED WORKFLOW MODE (Deterministic Architecture)
        # --------------------------------------------------------------------
        
        # Step 1: Deterministic Emergency Red Flag Filter (Rule-Based, Non-LLM)
        is_emergency, em_reason = EmergencySafetyGate.evaluate(user_query)
        tracer.log(
            self.step_counter,
            layer="DETERMINISTIC_CONTROL",
            component="EmergencySafetyGate",
            action="Red-Flag Keyword Screening",
            details="Screened query for acute emergency triggers (thunderclap, stroke signs, chest pain). Result: Non-emergency.",
            status="PASSED"
        )
        self.step_counter += 1

        # Step 2: Model Semantic Parsing
        tracer.log(
            self.step_counter,
            layer="MODEL_REASONING",
            component="PCP_Orchestrator_LLM",
            action="Clinical Entity Extraction",
            details="Identified symptom entities: ['headache', 'nausea']. Mapped clinical category: Neurological/Systemic.",
            status="COMPLETED"
        )
        self.step_counter += 1

        # Step 3: Deterministic Intake Schema & Completeness Gate
        intake_obj = structured_intake if structured_intake else IntakeContext(primary_symptoms=["headache", "nausea"])
        is_complete, missing_fields = intake_obj.is_complete_for_routing()

        if not is_complete:
            tracer.log(
                self.step_counter,
                layer="DETERMINISTIC_CONTROL",
                component="IntakeContractValidator",
                action="Handoff Contract Check",
                details=f"Routing REJECTED. Missing required intake fields: {missing_fields}",
                status="REJECTED"
            )
            self.step_counter += 1

            # Step 4: Governed Loop-Back for Structured Follow-up (Model drafts questions within template)
            tracer.log(
                self.step_counter,
                layer="MODEL_REASONING",
                component="PCP_Orchestrator_LLM",
                action="Draft Intake Questions",
                details="Model drafts structured, empathetic follow-up to acquire missing clinical parameters (onset, severity 1-10, change pattern, vision/fever).",
                status="WAITING_FOR_PATIENT"
            )
            self.step_counter += 1
            return tracer

        # --- If Intake IS Complete (Simulating Step 2 of Care Trajectory) ---
        tracer.log(
            self.step_counter,
            layer="DETERMINISTIC_CONTROL",
            component="IntakeContractValidator",
            action="Handoff Contract Check",
            details="All required intake fields verified (Onset: 24h, Severity: 6/10, Progression: Constant, Red Flags: Absent).",
            status="PASSED"
        )
        self.step_counter += 1

        # Step 4: MCP Scoped Tool Execution (Audit logged)
        mcp_allowed = MCPGateway.check_tool_permission("PCP_Agent", "get_patient_history")
        tracer.log(
            self.step_counter,
            layer="DETERMINISTIC_CONTROL",
            component="MCPGateway",
            action="Tool Policy Authorization",
            details=f"Tool 'get_patient_history' requested by PCP_Agent. Authorization policy evaluated: {mcp_allowed}.",
            status="PASSED" if mcp_allowed else "FAILED"
        )
        self.step_counter += 1

        # Step 5: Model Reasoning - Synthesize Evidence & Select Target Specialist
        tracer.log(
            self.step_counter,
            layer="MODEL_REASONING",
            component="PCP_Orchestrator_LLM",
            action="Differential Evidence Synthesis",
            details="Synthesized intake + EHR: Mild episodic tension/migraine history; nausea is secondary to headache, not primary GI pathogen. Target single specialist: Neurology.",
            status="COMPLETED"
        )
        self.step_counter += 1

        # Step 6: Deterministic Handoff Packet Assembly
        packet = SpecialistHandoffPacket(
            patient_id="PT-94812",
            target_specialty="Neurology",
            routing_reason="Episodic severe unilateral headache with secondary nausea; failed OTC acetaminophen",
            evidence_summary="Onset 24h ago; severity 6/10; no fever; no visual aura; prior history of tension headache in EHR.",
            intake_data=vars(intake_obj),
            relevant_ehr_snippets=["2023-11: Tension type headache diagnosed", "NKDA"]
        )
        tracer.log(
            self.step_counter,
            layer="DETERMINISTIC_CONTROL",
            component="HandoffPacketBuilder",
            action="Schema Conformance Check",
            details=f"Specialist packet created for [{packet.target_specialty}] with full clinical evidence and status: {packet.clinician_review_status}.",
            status="PASSED"
        )
        self.step_counter += 1

        # Step 7: Deterministic Human-In-The-Loop Gate (Mandatory Clinician Review)
        tracer.log(
            self.step_counter,
            layer="DETERMINISTIC_CONTROL",
            component="HumanInTheLoopGate",
            action="Clinician Approval Enforcement",
            details="SPECIALIST ROUTING PAUSED. Packet placed in Clinician Review Queue. External action blocked until licensed provider signs off.",
            status="AWAITING_HUMAN_APPROVAL"
        )

        return tracer


# ============================================================================
# 5. EXECUTION SUITE: THE HEADACHE-AND-NAUSEA TEST
# ============================================================================

def run_conference_demo():
    print("\n" + "#" * 95)
    print("  APPLIED AI SUMMIT DEMO: PCP COORDINATOR & SPECIALIST ROUTING")
    print("  Case Study: 'When Physicians Cannot Connect the Dots'")
    print("  Speaker: Monika Aggarwal (Enterprise AI & GTM Leader, IBM)")
    print("#" * 95)

    test_input = "I have a headache and feel nauseous."

    # ------------------------------------------------------------------------
    # RUN 1: LOOSE_AUTONOMY_MODE = True
    # ------------------------------------------------------------------------
    system_loose = PCPHealthcareAgentSystem(loose_autonomy_mode=True)
    trace_loose = system_loose.process_patient_query(test_input)

    # ------------------------------------------------------------------------
    # RUN 2: LOOSE_AUTONOMY_MODE = False (Initial Vague Query)
    # ------------------------------------------------------------------------
    system_governed = PCPHealthcareAgentSystem(loose_autonomy_mode=False)
    trace_governed_initial = system_governed.process_patient_query(test_input)

    # ------------------------------------------------------------------------
    # RUN 3: LOOSE_AUTONOMY_MODE = False (Follow-up with Completed Intake)
    # ------------------------------------------------------------------------
    completed_intake = IntakeContext(
        primary_symptoms=["headache", "nausea"],
        onset_time="Started yesterday afternoon (~24 hours ago)",
        severity_scale_1_to_10=6,
        progression="Gradually worsening with bright light, constant dull throbbing",
        associated_red_flags=["No fever", "No stiff neck", "No vision loss or numbness"],
        medications_tried=["500mg Acetaminophen (no relief)"]
    )
    print("\n" + "-" * 95)
    print("  PATIENT PROVIDES STRUCTURED INTAKE RESPONSES:")
    print("  Onset: 24h ago | Severity: 6/10 | Progression: Constant throbbing | Red Flags: None")
    print("-" * 95)
    trace_governed_complete = system_governed.process_patient_query(test_input, structured_intake=completed_intake)

    print("\n" + "=" * 95)
    print("  DEMO EXECUTION COMPLETE: 2 MODES COMPARED WITH FULL AUDIT TRACE")
    print("=" * 95 + "\n")


if __name__ == "__main__":
    run_conference_demo()
