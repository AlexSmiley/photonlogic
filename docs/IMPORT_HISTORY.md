# Import remaining historical snapshots

The development-history bundle **PhotonLogic-complete-research.zip** was created previously and is currently available for download in the ChatGPT conversation. It includes 32 recovered research snapshots and numerical assets. GitHub's connected write API cannot directly ingest the binary ZIP from the conversation sandbox, so the historical contents are **not yet transferred** to this repository.

To import locally:
```bash
git clone https://github.com/AlexSmiley/photonlogic.git
cd photonlogic
git checkout research/consolidated-photonlogic
# Extract PhotonLogic-complete-research.zip into a temporary directory
# Copy the extracted research/ directory into this repository's research/
git add research
git commit -m "Import historical PhotonLogic research snapshots"
git push origin research/consolidated-photonlogic
```

Preserve historical README versions and raw results; do not relabel modeled outputs as physical measurements. Avoid checking in secrets, oversized transient fields, caches, or confidential prefiling patent disclosures.
