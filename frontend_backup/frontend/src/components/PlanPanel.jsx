export default function PlanPanel() {
  return (
    <div className="h-full flex flex-col">
      <div className="px-5 py-4 border-b border-slate-800/50 bg-slate-900/30 backdrop-blur-sm">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-violet-500 animate-pulse" />
          <h2 className="text-base font-semibold text-slate-100 tracking-wide">Plan</h2>
        </div>
      </div>
      <div className="flex-1 p-4 flex flex-col gap-3">
        <textarea
          placeholder="Enter prompt..."
          className="flex-1 bg-slate-800/50 text-slate-100 border border-slate-700/50 rounded-xl p-4 resize-none focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500/50 placeholder-slate-500 transition-all text-sm leading-relaxed"
        />
        <button className="w-full bg-gradient-to-r from-violet-600 to-violet-500 hover:from-violet-500 hover:to-violet-400 text-white font-medium py-2.5 px-4 rounded-xl shadow-lg shadow-violet-900/20 hover:shadow-violet-900/30 transition-all duration-200 text-sm">
          Generate Plan
        </button>
      </div>
    </div>
  )
}
