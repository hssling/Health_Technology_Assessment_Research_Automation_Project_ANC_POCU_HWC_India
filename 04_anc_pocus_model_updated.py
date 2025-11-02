"""ANC PoCUS at HWC – decision model"""

anc_clients = 1000
hrp_prev = 0.12
baseline_usg_completion = 0.55
pocus_sensitivity = 0.85

cost_referral_usg = 600
cost_pocus_scan = 120
device_annualized_cost = 25000
training_cost_per_year = 5000

adv_outcome_no_early_detect = 0.08
adv_outcome_with_early_detect = 0.04

def strategy_current():
    hrp = anc_clients * hrp_prev
    detected = hrp * baseline_usg_completion
    adverse = (hrp - detected) * adv_outcome_no_early_detect + detected * adv_outcome_with_early_detect
    cost = anc_clients * baseline_usg_completion * cost_referral_usg
    return hrp, detected, adverse, cost

def strategy_pocus():
    hrp = anc_clients * hrp_prev
    detected = hrp * pocus_sensitivity
    adverse = (hrp - detected) * adv_outcome_no_early_detect + detected * adv_outcome_with_early_detect
    cost_scans = anc_clients * cost_pocus_scan
    referral_cost = detected * 0.7 * cost_referral_usg
    total_cost = cost_scans + device_annualized_cost + training_cost_per_year + referral_cost
    return hrp, detected, adverse, total_cost

if __name__ == "__main__":
    b_hrp, b_det, b_adv, b_cost = strategy_current()
    i_hrp, i_det, i_adv, i_cost = strategy_pocus()

    incr_cost = i_cost - b_cost
    incr_detected = i_det - b_det
    incr_adv_averted = b_adv - i_adv

    icer_detect = incr_cost / incr_detected if incr_detected > 0 else None
    icer_adverse = incr_cost / incr_adv_averted if incr_adv_averted > 0 else None

    print("Base:", b_hrp, b_det, b_adv, b_cost)
    print("Intervention:", i_hrp, i_det, i_adv, i_cost)
    print("ICER per HRP detected:", icer_detect)
    print("ICER per adverse outcome averted:", icer_adverse)
