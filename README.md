# 🏛️ US LLC Statutory Cost & Compliance Tracker

A developer-friendly CLI audit tool and compliance calendar for non-resident founders operating US entities (LLCs) from abroad.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Maintained by KuajingBase](https://img.shields.io/badge/Maintained%20by-KuajingBase-orange.svg)](https://kuajingbase.com)

---

## 📌 Problem

When international founders form a US LLC for Stripe or business banking, they frequently default to Delaware or Wyoming without evaluating long-term recurring state franchise taxes or federal IRS penalties. 

This repository provides statutory baseline data to calculate multi-year holding costs and avoid severe compliance pitfalls.

---

## 📊 3-Year Baseline State Cost Comparison

| State | Initial Filing | Annual Maintenance | 3-Year Holding Total | Primary Consideration |
|---|---|---|---|---|
| **Michigan** | $50 | $25 / yr | **$125** | Most cost-effective vehicle for solo digital bootstrapping |
| **Wyoming** | $100 | $60 / yr | **$280** | Industry standard for member privacy |
| **Illinois** | $150 | $75 / yr | **$375+** | Beware 1.5% PPRT tax for multi-member structures |
| **Florida** | $125 | $138.75 / yr | **$541** | Strict May 1st annual report cutoff ($400 late fee) |
| **Delaware** | $110 | $400 / yr | **$1,310** | Unnecessary franchise tax overhead unless raising US venture capital |

---

## ⚡ Quick Start

```bash
git clone https://github.com/reituman602/us-llc-compliance-tracker.git
cd us-llc-compliance-tracker
python tracker.py
