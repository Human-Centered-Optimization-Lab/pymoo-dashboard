/** @type {import('tailwindcss').Config} */
export default {
	content: [
		"./components/**/*.{js,vue,ts}",
		"./layouts/**/*.vue",
		"./pages/**/*.vue",
		"./plugins/**/*.{js,ts}",
		"./app.vue",
		"./error.vue",
	],
	theme: {
		extend: {
			animation: {
				openModal: '.2s ease-in forwards openmodal',
				closeModal: '.2s ease-out forwards closemodal',
			},
			keyframes: {
				openmodal: {
					'0%': { opacity: 0 },
					'100%': { opacity: 1, transform: 'translateY(-1rem)' }
				},
				closemodal: {
					'0%': { opacity: 1, transform: 'translateY(-1rem)' },
					'100%': { opacity: 0, transform: 'translateY(0)' }
				},

			}
		},
	},
	plugins: [],
}