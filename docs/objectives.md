| | MO-1 |
|---|---|
| What is measured | How long the class-count endpoint takes to answer for one task. |
| How | 5 runs. Each run sends 20 requests with curl and takes the median time. Raw output goes in docs/evidence/. |
| Target | TBD. I will measure the plain version first, then pick a target and explain why. |
| Conditions | My CPU is Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz. RAM is 15.85 GB. OS is Windows 10 Pro 64-bit. CVAT SHA is e4e93502ac5d4c8fd25834ee9e88dd3154ff7a22. There are 1000 images and 7204 annotations. Local Docker. Nothing else is running. |
| Not included | The very first request after a cold start. Video tasks. How long the page takes to draw. |

Results
Not measured yet.
