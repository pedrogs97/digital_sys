from celery import shared_task
from proposal.models import Proposal

@shared_task(
    bind=True,
    max_retries=5,
    default_retry_delay=30,
    track_started=True) 
def analyze_proposal(self, proposal_id): 
    try: 
        proposal = Proposal.objects.get(id=proposal_id)
        proposal.status=Proposal.ProposalStatus.APROVADA if proposal_id % 2 == 0 else Proposal.ProposalStatus.NEGADA
        proposal.save()
    except: 
        raise self.retry() 