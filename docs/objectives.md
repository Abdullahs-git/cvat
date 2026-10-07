| | MO-1 |
|---|---|
| What is measured | How long the class-count endpoint takes to answer for one task. |
| How | 5 runs. Each run sends 20 requests with a python benchmark script using urllib and takes the median time. Raw output goes in docs/evidence/mo1-benchmark.txt. |
| Target | < 500ms. Justification: Performing three subquery counts (labeledshape, labeledimage, labeledtrack) across a task's full relation tree of 8,109 objects via PostgreSQL is an expensive aggregation. A sub-500ms response time ensures that side-panel analytical components load smoothly for users without introducing noticeable lag. |
| Conditions | My CPU is Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz. RAM is 15.85 GB. OS is Windows 10.0.19045.0. CVAT SHA is 768dadede8d5a9ba1c2894e6bfb61b50a73de8d6 (with my custom branch changes). There are 1000 images and 8,109 annotations (after polygon split). Local Docker. Nothing else is running. |
| Not included | The very first request after a cold start (which is explicitly primed in the script). Video tasks. How long the page takes to draw. |

### Results
- **Overall 5-run Medians (ms):** 320.76, 332.67, 370.21, 392.27, 345.91
- **Final Overall Median (ms):** 345.91
- **Spread across runs (min-max) (ms):** 320.76 - 392.27
- *(See docs/evidence/mo1-benchmark.txt for the raw 100 request measurements)*
