Muhammad Abdullah Butt
Branch dev-test01
CVAT commit e4e93502ac5d4c8fd25834ee9e88dd3154ff7a22
7 October 2026
Start time 4:00 pm

What I am building
I am building an API that counts annotations per class for a task. I will also make a page that shows it as a graph. Then I will look at speed, one filter, and live updates if I get time.

What I count as one annotation
I count a shape as one. A tag is one. A track is one, not one per frame. The small parts of skeleton shapes are not counted on their own. Classes with zero annotations still show up with 0. This way the page can tell "no data" from "empty class". I think this matches how CVAT stores things but I have not checked the models yet. Note: one occluded COCO object can become several CVAT polygons (7,204 JSON annotations became 8,109 CVAT shapes).

My time plan
Setup happens before this and is not in the table. This includes Docker, download and import.

0:00-0:30 write docs and commit them
0:30-1:30 read the CVAT models, write the count in raw SQL first
1:30-2:45 Django app called "test", the endpoint, login and permissions
2:45-4:15 the page, the graph, empty and error cases
4:15-5:00 speed: measure first, then set one target
5:00-5:30 one filter or grouping
5:30-7:00 WebSocket and reconnect, stop when time is up
7:00-8:00 final docs, Loom video, pull request

Rules for myself
Items 1 to 4 must work before I touch anything else. If items 1 to 7 are not proven by hour 5, I skip the WebSocket and say so honestly. At hour 7 I stop coding.

How I plan to do it
I will do the counting in the database with a group by. I will put this in a separate service file, not in the view. I will use CVAT's own login and its existing task permission code instead of writing my own checks. I will put the endpoint under its own URL so it does not clash with the existing tasks routes. I will make one page and one route in the UI. I will use a chart library already in the project if there is one. Otherwise I will draw simple bars myself. I have not checked any of this in the code yet.

What I will skip
I will skip caching. I will skip changing the permission rules. I will skip project level counts. I will skip video tasks. I will skip pagination. I will skip mobile layout.

What could go wrong
Rebuilding the server and UI from source may be slow or annoying. I think CVAT has no WebSocket support set up, so that part may need big changes. I think annotations are saved in bulk, so normal Django signals may not fire. Imports probably run in a worker process, not the web process. I will check each of these.

Decision record
I will fill this in at the end: what I chose, what I did not choose, and what that cost me.

Changes to the plan
Dated notes here if I change the plan, with the reason.
