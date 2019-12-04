
from uperations.kernel import Kernel
from uperation_base import Base
from libraries.ticketmaster.ticketmaster import Ticketmaster
from libraries.eventbrite.eventbrite import Eventbrite
from libraries.meetup.meetup import Meetup
from libraries.admin.admin import Admin

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base(),
        Ticketmaster.name(): Ticketmaster(),
        Eventbrite.name(): Eventbrite(),
        Meetup.name(): Meetup(),
        Admin.name(): Admin()
    })

    Kernel.get_instance().set_observers({
        #operation().__class__ : [
        #   observer().__class__
        # ]
    })
