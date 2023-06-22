from celery import shared_task
from proposal.models import Proposal

@shared_task(
    bind=True,
    max_retries=5,
    default_retry_delay=30,
    track_started=True) 
def analyze_proposal(self, proposal_id): 
    try: 
        Proposal.objects.update(status=Proposal.ProposalStatus.APROVADA if proposal_id % 2 == 0 else Proposal.ProposalStatus.NEGADA)
    except: 
        raise self.retry() 