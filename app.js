const tasks = [
  { id: 1, title: "Buy milk", done: true, priority: "low" },
  { id: 2, title: "Study JavaScript", done: false, priority: "high" },
  { id: 3, title: "Push to GitHub", done: false, priority: "high" },
  { id: 4, title: "Clean the room", done: true, priority: "high" },
  { id: 5, title: "Call Fatima", done: false, priority: "low" },
];


const countOpen = (tasks) => tasks.filter((t) => !t.done).length;


const titlesByPriority = (tasks, priority) =>
  tasks.filter((t) => t.priority === priority).map((t) => t.title);

console.log(countOpen(tasks)); // 3
console.log(titlesByPriority(tasks, "high"));