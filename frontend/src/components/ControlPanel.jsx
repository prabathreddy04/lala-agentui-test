export default function ControlPanel() {
  return (
    <div className="h-full flex flex-col border-l border-slate-800/50">
      <div className="px-5 py-4 border-b border-slate-800/50 bg-slate-900/30 backdrop-blur-sm">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-amber-500 animate-pulse" />
          <h2 className="text-base font-semibold text-slate-100 tracking-wide">Control</h2>
        </div>
      </div>
      <div className="flex-1 p-4 flex flex-col gap-5">
        <div className="bg-slate-800/30 rounded-xl p-4 border border-slate-700/30">
          <label className="block text-xs font-medium text-slate-400 mb-3 uppercase tracking-wider">Reasoning Mode</label>
          <div className="flex items-center justify-between">
            <span className="text-sm text-slate-300">Extended</span>
            <div className="relative">
              <div className="w-14 h-7 bg-slate-700 rounded-full cursor-pointer shadow-inner">
                <div className="absolute right-1 top-1 w-5 h-5 bg-gradient-to-br from-white to-slate-200 rounded-full shadow-md" />
              </div>
            </div>
          </div>
        </div>
        <div className="bg-slate-800/30 rounded-xl p-4 border border-slate-700/30">
          <label className="block text-xs font-medium text-slate-400 mb-3 uppercase tracking-wider">Token Quota</label>
          <div className="relative">
            <input
              type="number"
              placeholder="100000"
              className="w-full bg-slate-900/50 text-slate-100 border border-slate-600/50 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-amber-500/20 focus:border-amber-500/50 text-sm font-mono transition-all"
            />
            <span className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-500">tokens</span>
          </div>
        </div>
        <div className="mt-auto">
          <button className="w-full bg-gradient-to-r from-rose-600 to-red-500 hover:from-rose-500 hover:to-red-400 text-white font-medium py-2.5 px-4 rounded-xl shadow-lg shadow-rose-900/20 hover:shadow-rose-900/30 transition-all duration-200 text-sm">
            Take Over Control
          </button>
        </div>
      </div>
    </div>
  )
}
