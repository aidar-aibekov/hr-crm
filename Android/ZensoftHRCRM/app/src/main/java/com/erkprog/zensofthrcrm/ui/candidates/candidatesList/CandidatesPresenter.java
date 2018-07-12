package com.erkprog.zensofthrcrm.ui.candidates.candidatesList;

import com.erkprog.zensofthrcrm.data.entity.Candidate;
import com.erkprog.zensofthrcrm.data.entity.CandidatesResponse;
import com.erkprog.zensofthrcrm.data.network.remote.ApiInterface;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CandidatesPresenter implements CandidatesContract.Presenter {

  private CandidatesContract.View mView;
  private ApiInterface mApiService;

  CandidatesPresenter(ApiInterface service) {
    mApiService = service;
  }

  @Override
  public void loadCandidates() {
    mApiService.getCandidates().enqueue(new Callback<CandidatesResponse>() {
      @Override
      public void onResponse(Call<CandidatesResponse> call, Response<CandidatesResponse> response) {
        if (isViewAttached()) {
          if (response.isSuccessful() && response.body().getCandidateList() != null) {
            mView.showCandidates(response.body().getCandidateList());
          } else {
            mView.showMessage("Candidates list in response is null");
          }
        }
      }

      @Override
      public void onFailure(Call<CandidatesResponse> call, Throwable t) {
        if (isViewAttached()) {
          mView.showMessage(t.getMessage());
        }
      }
    });
  }

  private boolean isViewAttached() {
    return mView != null;
  }

  @Override
  public void onCandidateItemClick(Candidate candidate) {
    mView.showCandidateDetailUi(candidate.getId());
  }

  @Override
  public void bind(CandidatesContract.View view) {
    mView = view;
  }

  @Override
  public void unbind() {
    mView = null;
  }
}
