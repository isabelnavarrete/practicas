
const BookingEngine = function () {
    return {
        init: function () {
            this.$startDate = $('#diaE')
            this.$endDate = $('#diaS')

            const minDate = new Date().toISOString().split('T')[0]
            this.$startDate.attr('min', minDate)
            this.$startDate.val(minDate)
            this.$endDate.attr('min', minDate)
            this.$endDate.val(minDate)
        }
    }
}();

export default BookingEngine