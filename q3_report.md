# Q3 – Native Language Voice Bot Prototype

## Objective

Develop localized conversational bot prototypes for:

1. Philippines
2. Indonesia

The solution demonstrates localized language handling, code-switching support, and market-specific terminology.

---

## Philippines Bot

### Supported Languages

- English
- Filipino
- Taglish

### Example Terms

- Premium
- Policy
- Beneficiary
- Coverage
- Rider

### Design Considerations

- Natural Taglish conversations
- Respectful tone
- Local insurance terminology
- Safe fallback responses

---

## Indonesia Bot

### Supported Languages

- Bahasa Indonesia
- Informal conversational Indonesian

### Example Terms

- Tenor
- DP
- Cicilan
- Pembiayaan

### Design Considerations

- Local finance terminology
- Natural conversational style
- Safe fallback responses
- Human escalation support

---

## Code Switching

The prototype supports mixed-language customer interactions.

Examples:

Philippines:

- "Magkano ang premium?"
- "Can I update my beneficiary?"

Indonesia:

- "Berapa tenor?"
- "Saya belum bisa bayar cicilan."

---

## Testing

The implementation was tested using multiple representative customer scenarios.

### Philippines

- Premium inquiry
- Beneficiary inquiry
- Coverage inquiry
- Payment inquiry
- Policy support

### Indonesia

- Tenor inquiry
- DP inquiry
- Installment inquiry
- Human assistance
- Application status inquiry

---

## Limitations

This prototype uses rule-based localization examples.

A production implementation would include:

- Real ASR
- Real TTS
- Regional dialect support
- Intent classification
- Human handoff workflows
- Retrieval-based knowledge grounding

---

## Conclusion

The prototype demonstrates localized conversational behavior for the Philippines and Indonesia markets while supporting local terminology and code-switching patterns.